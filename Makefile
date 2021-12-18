test:
	cp requirements.txt functions/$(function)
	cd functions/$(function)/; functions-framework --port 9090 --target=main

deploy:
	cp requirements.txt functions/$(function)
	cd functions/$(function)/; gcloud functions deploy $(function) --entry-point main --runtime python39 --trigger-http --project=$(project) --allow-unauthenticated
