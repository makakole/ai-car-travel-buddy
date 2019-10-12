import os
import sys
args = sys.argv
directory = args[1]
protoc_path = args[2]
for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+directory+"/"+file+" --python_out=.")


# /home/mk/dev/ai-car-travel-buddy/obj-detection/models/research/object_detection/protos

# /home/mk/Downloads/protobuf-python-3.10.0/protobuf-3.10.0/cmake/protoc.cmake

# x-special/nautilus-clipboard
# copy
# file:///home/mk/Downloads/protoc-3.10.0-linux-x86_64/bin/protoc




# python use_protobuf.py /home/mk/dev/ai-car-travel-buddy/obj-detection/models/research/object_detection/protos /home/mk/Downloads/protoc-3.10.0-linux-x86_64/bin/protoc
# Example: python use_protobuf.py object_detection/protos C:/Users/Gilbert/Downloads/bin/protoc

x-special/nautilus-clipboard
copy
file:///home/mk/dev/ai-car-travel-buddy/obj-detection/models/research/slim


# export PYTHONPATH=$PYTHONPATH:/home/mk/dev/ai-car-travel-buddy/obj-detection/models/research/
# export PYTHONPATH=$PYTHONPATH:/home/mk/dev/ai-car-travel-buddy/obj-detection/models/research/object_detection/
# export PYTHONPATH=$PYTHONPATH:/home/mk/dev/ai-car-travel-buddy/obj-detection/models/research/slim