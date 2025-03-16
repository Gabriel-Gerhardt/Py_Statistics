import warnings

# Ignore NotOpenSSLWarning
warnings.filterwarnings("ignore", message=".*NotOpenSSLWarning.*")

# Your code that triggers the warning
import urllib3
# Example code using urllib3 that triggers the warning