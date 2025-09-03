FROM python:3.9-bullseye

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies with Java 17
RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME for Java 17
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Upgrade pip and install Python packages
RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install buildozer cython==0.29.33

# Create working directory
WORKDIR /app

# Copy project files
COPY . /app

# Make build script executable
RUN chmod +x /app/build.sh

# Initialize buildozer and build (with non-interactive flag)
CMD ["bash", "/app/build.sh"]