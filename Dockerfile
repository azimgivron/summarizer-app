# Use ARM64 Debian Bookworm as the base image
FROM --platform=linux/arm64 debian:bookworm

# Environment variables
ENV HOSTNAME=summarizer-server
ENV DEBIAN_FRONTEND=noninteractive
ENV USERNAME=ai_user
ENV VENV_NAME=summarizer_venv
ENV VENV_PATH="/home/$USERNAME/$VENV_NAME"
ENV PATH="$VENV_PATH/bin:$PATH"

# Install system dependencies, Python, and Zsh
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    git curl wget build-essential sudo zsh unzip \
    && rm -rf /var/lib/apt/lists/*

# Create a new user and set up Zsh with Oh My Zsh
RUN useradd -m -s /bin/zsh $USERNAME && \
    usermod -aG sudo $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    sh -c "echo '$HOSTNAME' > /etc/hostname" && \
    wget https://github.com/ohmyzsh/ohmyzsh/archive/refs/heads/master.zip -O /tmp/ohmyzsh.zip && \
    unzip /tmp/ohmyzsh.zip -d /tmp && \
    mv /tmp/ohmyzsh-master /home/$USERNAME/.oh-my-zsh && \
    cp /home/$USERNAME/.oh-my-zsh/templates/zshrc.zsh-template /home/$USERNAME/.zshrc && \
    rm -rf /tmp/ohmyzsh.zip /tmp/ohmyzsh-master && \
    chown -R $USERNAME:$USERNAME /home/$USERNAME/.oh-my-zsh /home/$USERNAME/.zshrc

# Switch to the new user
USER $USERNAME

# Set working directory
WORKDIR /home/$USERNAME

# Copy the project files and pre-install dependencies to avoid errors
RUN python3 -m venv $VENV_PATH && \
    $VENV_PATH/bin/pip install --upgrade pip

# Add virtual environment activation to Zsh
RUN echo "alias activate=$VENV_PATH/bin/activate" >> /home/$USERNAME/.zshrc

# Expose application port
EXPOSE 8080

# Set Zsh as the default shell and start the application
SHELL ["/bin/zsh", "-c"]
CMD ["zsh"]
