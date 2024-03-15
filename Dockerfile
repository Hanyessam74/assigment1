# Specify the base image as Ubuntu
FROM ubuntu

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container at /home/doc-bd-a1/
RUN mkdir /home/doc-bd-a1/

# Move the dataset file to the container
COPY load.py /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/ 
COPY vis.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/
# Set the working directory
WORKDIR /home/doc-bd-a1/

# Open the bash shell upon container startup
CMD ["/bin/bash"]


