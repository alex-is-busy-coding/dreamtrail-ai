# Use the official Node.js image as the base image
FROM node:20.18-slim

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Set build-time argument for environment (default to production)
ARG ENVIRONMENT=production

# Install dependencies based on the ENVIRONMENT
# If ENVIRONMENT is "development", install all dependencies, otherwise omit dev dependencies
RUN if [ "$ENVIRONMENT" = "development" ]; \
    then npm install; \
    else npm install --omit=dev; \
    fi

# Copy the rest of the application files
COPY . .

# Build the Next.js app if in production mode
RUN if [ "$ENVIRONMENT" = "production" ]; then npm run build; fi

# Expose port 3000 for the application
EXPOSE 3000

# Disable Next.js telemetry
ENV NEXT_TELEMETRY_DISABLED 1

# Command to run the application based on ENVIRONMENT
CMD ["sh", "-c", "if [ \"$ENVIRONMENT\" = \"development\" ]; then npm run dev; else npm run start; fi"]