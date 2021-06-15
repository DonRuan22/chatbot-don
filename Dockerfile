#whatever version that suits you
FROM rasa/rasa-sdk:latest 

#define the working directory of Docker container
WORKDIR /app 

#copy everything in ./actions directory (your custom actions code) to /app/actions in container
COPY ./ ./

# Run the generated shell script.
ENTRYPOINT ["entrypoint.sh"]