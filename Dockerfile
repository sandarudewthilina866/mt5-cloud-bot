FROM ubuntu:22.04

# Install Wine and Python dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y wine32 wine64 python3 python3-pip xvfb wget && \
    apt-get clean

# Set up working directory
WORKDIR /app

# Copy python files
COPY . /app

# Install MetaTrader5 Python library
RUN pip3 install --no-cache-dir MetaTrader5

# Run the bot using Xvfb (Virtual Framebuffer for GUI-less Wine)
CMD ["xvfb-run", "-a", "python3", "bot.py"]
