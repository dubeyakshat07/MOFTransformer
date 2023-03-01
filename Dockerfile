FROM pytorch/pytorch
MAINTAINER "akshat"

# RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
# RUN bash Anaconda3-2022.05-Linux-x86_64.sh

RUN conda create -n predict python=3.10 anaconda
RUN conda init bash --user && \
conda activate predict

RUN pip install -r requirements.txt
RUN apt install build-essential -y

RUN git clone https://github.com/Sangwon91/GRIDAY.git && \
cd GRIDAY && \
make && \
cd ..






