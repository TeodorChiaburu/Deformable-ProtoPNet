base_architecture = 'resnet50' # will load inat weights if told so in resnet_features.py:L258
img_size = 224
num_classes = 22

experiment_run = '013'

# Full set: './datasets/CUB_200_2011/'
# Cropped set: './datasets/cub200_cropped/'
# Stanford dogs: './datasets/stanford_dogs/'
data_path = '../../data/Wildbienen/'

train_dir = data_path + 'Bees_bbox_train/'
# Cropped set: train_cropped & test_cropped
# Full set: train & test
test_dir = data_path + 'Bees_bbox_val/'
train_push_dir = data_path + 'Bees_bbox_train/'
train_batch_size = 80
test_batch_size = 100
train_push_batch_size = 75

joint_optimizer_lrs = {'features': 1e-4,
                       'add_on_layers': 3e-3,
                       'prototype_vectors': 3e-3,
                       'conv_offset': 5e-5, #5e-3,#5e-4,
                       'joint_last_layer_lr': 1e-5}
joint_lr_step_size = 2 #5

warm_optimizer_lrs = {'add_on_layers': 3e-3,
                      'prototype_vectors': 3e-3}

warm_pre_offset_optimizer_lrs = {'add_on_layers': 3e-3,
                      'prototype_vectors': 3e-3,
                      'features': 1e-4}

warm_pre_prototype_optimizer_lrs = {'add_on_layers': 3e-3,
                      'conv_offset': 3e-4, #3e-2, #3e-3,
                      'features': 1e-4}

last_layer_optimizer_lr = 1e-4
last_layer_fixed = True

coefs = {
    'crs_ent': 1,
    'clst': -0.8,
    'sep': 0.08,
    'l1': 1e-2,
    'offset_bias_l2': 8e-1,
    'offset_weight_l2': 8e-1,
    'orthogonality_loss': 0.1
}

subtractive_margin = True

num_train_epochs = 7 #21
num_warm_epochs = 1 #2
num_secondary_warm_epochs = 1 #2
push_start = 2 #4

push_epochs = [i for i in range(num_train_epochs) if i % 3 == 0]
