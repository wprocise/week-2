# Use the repository name "<username>/<assignment-name>:[tag]"
    # tags: latest, template, exercise-1, exercise-2, etc.

# ------------------------------- BUILD COMMAND ------------------------------ #
# docker build --platform linux/amd64,linux/arm64 -t <username>/<assignment-name>:[tag] .
# ------------------------------- BUILD COMMAND ------------------------------ #


# --------------- DEBUGGING COMMAND (run from parent directory) -------------- #
# docker run --rm -it -v ./:/autograder/submission -v ./autograder:/autograder/results <username>/<assignment-name>:[tag] bash
# --------------- DEBUGGING COMMAND (run from parent directory) -------------- #


# (see https://gradescope-autograders.readthedocs.io/en/latest/manual_docker/)

# ---------------------------------------------------------------------------- #
#                                   autograder                                 #
# ---------------------------------------------------------------------------- #
# see https://github.com/gradescope/autograder_samples/blob/master/manual_docker
# also see https://hub.docker.com/r/gradescope/autograder-base/tags/
FROM gradescope/autograder-base:latest

# Copy the autograder script into the container
COPY run_autograder /autograder/

# Ensure script is Unix-friendly and executable
RUN dos2unix /autograder/run_autograder
RUN chmod +x /autograder/run_autograder

# Copy the tests into the container
COPY tests /autograder/tests
COPY run_tests.py /autograder/

# Copy default results.json file, which will be overwritten upon grading
COPY results.json /autograder/results/

# ---------------------------------------------------------------------------- #
#                                   miniconda                                  #
# ---------------------------------------------------------------------------- #
# see https://www.anaconda.com/docs/getting-started/miniconda/install#linux
# also see https://www.anaconda.com/docs/reference/troubleshooting
# Adjustments: 
#     bash -c "source ~/miniconda3/bin/activate" (bash explicit)
#     ~/miniconda3/bin/conda init --all bash (see troubleshooting, above)
RUN mkdir -p ~/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
RUN rm ~/miniconda3/miniconda.sh
RUN bash -c "source ~/miniconda3/bin/activate"
RUN ~/miniconda3/bin/conda init --all bash

# --------------------------- Pre-install packages --------------------------- #
# Copy environment.yml
COPY environment.yml /autograder/

# install environment packages
RUN ~/miniconda3/bin/conda env update -n base -f /autograder/environment.yml --prune

# install gradescope-utils for autograder 
RUN ~/miniconda3/bin/pip install gradescope-utils