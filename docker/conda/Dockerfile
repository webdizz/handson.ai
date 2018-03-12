FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

RUN apt-get update \
	&& apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
	&& apt-get install -y libgomp1 vim
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
	wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
	/bin/bash ~/miniconda.sh -b -p /opt/conda && \
	rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

COPY ./environment.yml /environment.yml

RUN conda env create -f /environment.yml \
	&& mkdir -p /opt/notebooks

VOLUME "/opt/notebooks"

CMD ["/opt/conda/envs/handson.ai/bin/jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser"]

EXPOSE 8888
