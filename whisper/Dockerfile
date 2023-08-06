# ARG FUNCTION_DIR="/function"
# FROM python:3.10 as build-image

# # Include global arg in this stage of the build
# ARG FUNCTION_DIR

# # Copy function code
# RUN mkdir -p ${FUNCTION_DIR}
# COPY . ${FUNCTION_DIR}

# # Install the function's dependencies
# RUN pip install --target ${FUNCTION_DIR} -r ${FUNCTION_DIR}/requirements.txt
# RUN pip install --target ${FUNCTION_DIR} "git+https://github.com/openai/whisper.git" 
# # RUN apt-get install -y ffmpeg

# # Use a slim version of the base Python image to reduce the final image size
# FROM python:3.10-slim

# # Include global arg in this stage of the build
# ARG FUNCTION_DIR

# # Set working directory to function root directory
# WORKDIR ${FUNCTION_DIR}

# # Copy in the built dependencies
# COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

# # Set runtime interface client as default command for the container runtime
# ENTRYPOINT [ "python3", "-m", "awslambdaric" ]

# # Pass the name of the function handler as an argument to the runtime
# CMD [ "lamda_function.handler" ]

FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY . ${LAMBDA_TASK_ROOT}

RUN pip install --target ${LAMBDA_TASK_ROOT} -r ${LAMBDA_TASK_ROOT}/requirements.txt
# RUN pip install --target ${LAMBDA_TASK_ROOT} "git+https://github.com/openai/whisper.git" 

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lamda_function.handler" ]
