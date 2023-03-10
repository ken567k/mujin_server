FROM debian:bullseye


# Install the required packages
RUN apt update
RUN apt-get install -y libprotobuf-dev protobuf-compiler cmake git g++ minizip vim
RUN apt-get install -y software-properties-common
RUN apt-get install -y libassimp-dev libavcodec-dev libavformat-dev libavformat-dev libboost-all-dev libboost-date-time-dev libbullet-dev libglew-dev libgsm1-dev liblapack-dev liblog4cxx-dev libmpfr-dev libode-dev libogg-dev libpcrecpp0v5 libpcre3-dev libqhull-dev libsoqt520-dev libswscale-dev libswscale-dev libvorbis-dev libx264-dev libxml2-dev libxvidcore-dev libeigen3-dev libccd-dev libasio-dev libcpprest-dev

RUN apt-get install -y python3-dev python-dev python3-numpy python python-pkg-resources python2.7
RUN apt-get install -y python3-opengl 

RUN apt-get -y install libboost-atomic-dev libboost-thread-dev libboost-system-dev  
RUN apt-get -y install libboost-date-time-dev libboost-regex-dev 
RUN apt-get -y install libboost-filesystem-dev libboost-random-dev libboost-chrono-dev 
RUN apt-get -y install libboost-serialization-dev libwebsocketpp-dev 
RUN apt-get -y install openssl libssl-dev ninja-build

RUN git clone https://github.com/rdiankov/collada-dom.git
RUN cd collada-dom && mkdir build && cd build && \
    cmake .. && \
    make -j4 && \
    make install

RUN git clone https://github.com/Tencent/rapidjson.git
RUN cd rapidjson &&  mkdir build && cd build && \
    cmake .. && \
    make -j4 && \
    make install

#RUN git clone https://github.com/pybind/pybind11.git
#RUN cd pybind11 && \
#   git cherry-pick 94824d68a037d99253b92a5b260bb04907c42355 98c9f77e5481af4cbc7eb092e1866151461e3508  && \
#   mkdir build && cd build && \
#   cmake .. && \
#   make -j4 && \
#   make install

RUN git config --global user.email "docker@example.com"
RUN git config --global user.name "docker"
RUN git clone https://github.com/pybind/pybind11.git  && \
    cd pybind11 && mkdir build && cd build  && \
    git remote add woody https://github.com/woodychow/pybind11.git \
        && git fetch woody && git checkout v2.2.4 \
        && git cherry-pick 94824d68a037d99253b92a5b260bb04907c42355 \
        && git cherry-pick 98c9f77e5481af4cbc7eb092e1866151461e3508 \
        && cmake .. -DPYBIND11_TEST=OFF -DPythonLibsNew_FIND_VERSION=2 \
        && make install

#RUN apt-get -y install libcairo2-dev libpoppler-glib-dev libsdl2-dev libtiff5-dev libxrandr-dev
#RUN git clone --branch OpenSceneGraph-3.4 https://github.com/openscenegraph/OpenSceneGraph.git
#RUN cd OpenSceneGraph && mkdir build && cd build && \
#   cmake .. -DDESIRED_QT_VERSION=4 && \
#   make -j4 && \
#   make install

#RUN git clone https://github.com/flexible-collision-library/fcl.git
#RUN cd fcl && git checkout 0.5.0 && mkdir build && cd build && \
#   cmake .. && \
#   make -j4 && \
#   make install

RUN ln -sf /usr/include/eigen3/Eigen /usr/include/Eigen
RUN export OPENRAVE_PLUGINS="/usr/local/share/openrave-0.9/plugins:${OPENRAVE_PLUGINS}"


RUN apt-get -y install curl
RUN curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py && \
    python3 get-pip.py && \
    pip install ipython h5py numpy scipy wheel && \
    rm get-pip.py

RUN apt-get -y install libboost-all-dev libboost-python-dev
#libboost-python-dev=boost_1_58_0

# Set the working directory
WORKDIR /app

# Copy required files
COPY /. open_rave_src

# Build the application with cmake
#RUN cd /app/open_rave_src && \
#   cmake .
#RUN mkdir /app/open_rave_src/build && cd /app/open_rave_src/build && \
#   cmake .

#RUN cd /app/open_rave_src/build && \
#   cmake .. && \
#   make install

RUN cd /app/open_rave_src/build && \
    cmake -DODE_USE_MULTITHREAD=ON -DOSG_DIR=/usr/local/lib64/ \
        -DUSE_PYBIND11_PYTHON_BINDINGS:BOOL=TRUE              .. && \
        #-DBoost_NO_BOOST_CMAKE=1 .. &&\
        #-DBoost_NO_WARN_NEW_VERSIONS=1 \
        #-DCMAKE_BUILD_TYPE=RelWithDebInfo && \
    make -j4 && \
    make install