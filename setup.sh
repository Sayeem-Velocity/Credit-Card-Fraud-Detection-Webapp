#!/bin/bash

# Create Streamlit config directory
mkdir -p ~/.streamlit/

# Write Streamlit config file
echo "\
[server]
headless = true
port = \$PORT
enableCORS = false
enableXsrfProtection = false
" > ~/.streamlit/config.toml