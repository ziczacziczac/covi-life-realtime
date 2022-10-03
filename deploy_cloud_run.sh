docker build --build-arg EXTRA_REPO_URL=https://oauth2accesstoken:$(gcloud auth print-access-token)@asia-south1-python.pkg.dev/glassy-totality-324307/covi-life-repository/simple . -t=globicare-realtime:latest --no-cache
docker tag globicare-realtime gcr.io/glassy-totality-324307/globicare-realtime
gcloud docker -- push gcr.io/glassy-totality-324307/globicare-realtime
gcloud run deploy globicare-realtime --image gcr.io/glassy-totality-324307/globicare-realtime --region=asia-south1 --allow-unauthenticated --vpc-connector=covi-life-mongo-connector --vpc-egress=all-traffic