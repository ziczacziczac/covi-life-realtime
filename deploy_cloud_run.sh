gcloud secrets add-iam-policy-binding DATABASE_NAME --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding USER_SECRET --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding DEVICE_SECRET --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding USER_TABLE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding REGISTER_TABLE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding FIREBASE_SECRET --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding AVATAR_BUCKET --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding OTP_SENDER --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding OTP_KEYWORD --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding OTP_MESSAGE_TEMPLATE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding OTP_SECRET_KEY --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding OTP_PARTNER_CODE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding OTP_LOGGING_TABLE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding AVARTAR_COVI_LIFE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding MONGO_SERVER --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding USER_AVATAR_BUCKET --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding USER_AVARTAR_COVI_LIFE --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud secrets add-iam-policy-binding NUMBER_PATIENT_LIMITED --role roles/secretmanager.secretAccessor --member serviceAccount:693115483107-compute@developer.gserviceaccount.com
gcloud projects add-iam-policy-binding glassy-totality-324307 --member serviceAccount:693115483107-compute@developer.gserviceaccount.com --role roles/artifactregistry.reader

docker build --build-arg EXTRA_REPO_URL=https://oauth2accesstoken:$(gcloud auth print-access-token)@asia-south1-python.pkg.dev/glassy-totality-324307/covi-life-repository/simple . -t=covi-life-realtime:latest --no-cache
docker tag covi-life-realtime gcr.io/glassy-totality-324307/covi-life-realtime
gcloud docker -- push gcr.io/glassy-totality-324307/covi-life-realtime
gcloud run deploy covi-life-realtime --image gcr.io/glassy-totality-324307/covi-life-realtime --region=asia-south1 --allow-unauthenticated --vpc-connector=covi-life-mongo-connector --vpc-egress=all-traffic