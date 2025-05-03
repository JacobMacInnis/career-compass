#!/bin/bash

# Load environment variables
set -o allexport
# source $(dirname "$0")/.env
source "$(dirname "$0")/../.env"
set +o allexport

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function for printing with color
function echo_success() { echo -e "${GREEN}$1${NC}"; }
function echo_warning() { echo -e "${YELLOW}$1${NC}"; }
function echo_error() { echo -e "${RED}$1${NC}"; }

# Read user option
OPTION=$1

if [[ -z "$OPTION" ]]; then
  echo_warning "No deployment option provided!"
  echo_warning "Please choose an option:"
  echo "1) full (prepare data, train model, deploy)"
  echo "2) train-and-deploy (train model, deploy)"
  echo "3) deploy (only build and deploy)"

  read -p "Enter your choice (1/2/3): " choice
  case $choice in
    1) OPTION="full" ;;
    2) OPTION="train-and-deploy" ;;
    3) OPTION="deploy" ;;
    *) echo_error "Invalid choice. Exiting."; exit 1 ;;
  esac
fi

echo_success "🚀 Starting '$OPTION' deployment..."

# Step 1: Data Preparation
if [[ "$OPTION" == "full" ]]; then
  echo_success "🔧 Running data preparation..."
  python src/data_preparation.py || { echo_error "Data preparation failed!"; exit 1; }
fi

# Step 2: Model Training
if [[ "$OPTION" == "full" || "$OPTION" == "train-and-deploy" ]]; then
  echo_success "🧠 Training model..."
  python src/model_training.py || { echo_error "Model training failed!"; exit 1; }
fi

# Step 3: Docker build
echo_success "🐳 Building Docker image..."
docker build --platform=linux/amd64 -t ${IMAGE_NAME}:latest . || { echo_error "Docker build failed!"; exit 1; }

# Step 4: Docker tag
echo_success "🏷️ Tagging Docker image..."
docker tag ${IMAGE_NAME}:latest ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_REPO}/${IMAGE_NAME}:latest

# Step 5: Docker push
echo_success "📦 Pushing Docker image to Artifact Registry..."
docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_REPO}/${IMAGE_NAME}:latest || { echo_error "Docker push failed!"; exit 1; }

# Step 6: Cloud Run deploy
echo_success "☁️ Deploying to Cloud Run..."
gcloud run deploy ${CLOUD_RUN_SERVICE_NAME} \
  --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_REPO}/${IMAGE_NAME}:latest \
  --platform managed \
  --region ${GCP_REGION} \
  --allow-unauthenticated \
  --port ${PORT} \
  --memory ${CLOUD_RUN_MEMORY} \
  --timeout ${CLOUD_RUN_TIMEOUT}s || { echo_error "Cloud Run deployment failed!"; exit 1; }

echo_success "✅ Deployment completed successfully!"

# Optional: Auto-clean dangling docker images
echo_warning "🧹 Cleaning up dangling Docker images..."
docker image prune -f
