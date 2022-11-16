FROM ubuntu:18.04

LABEL Suheel Yousuf Wani <suheelhamdani@gmail.com>

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install build-essential wget
RUN apt-get install --no-install-recommends --no-install-suggests -y python


RUN apt-get install -y curl

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;
    
ENV URL=http://www.bioinformatics.babraham.ac.uk/projects/fastqc

ENV ZIP=fastqc_v0.11.9.zip

RUN apt-get update && apt-get -y install fastqc;

RUN apt-get update && apt-get -y install trimmomatic;

RUN  wget http://cab.spbu.ru/files/release3.15.0/SPAdes-3.15.5.tar.gz -O /tmp/spades.tar.gz && \
     tar -xvzf /tmp/spades.tar.gz -C /opt/ && \
     rm /tmp/spades.tar.gz
     
RUN apt-get install --no-install-recommends --no-install-suggests -y cmake make g++ zlib1g-dev libbz2-dev bzip2 libz-dev

RUN apt-get -y autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

RUN cd /opt/SPAdes-3.15.5/ && ./spades_compile.sh

ENV PATH="/opt/SPAdes-3.15.5/:${PATH}"

RUN apt-get update && apt-get -y install bwa




