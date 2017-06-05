n_classes = 2
numEpochs = 2000
numChannels = 3

batch_size = 32
testTrainSplit = 0.8
imageSizeX=224
imageSizeY=224
training_keep_rate = 0.9
testing_keep_rate = 1.0

ckpt_dir = "./model"
pretrainedModelPath = "./pretrainedModel/vgg16.npy"

# This flag controls if the pretrained vgg16 network would be used for feature extraction.
usePretrainedNetwork = True
# This flag controls if the pretrained network would also be fine-tuned.
fineTunePretrainedModel = False

# The folder where the dataset resides.
datasetFolder = "cifar10DatasetSample"
