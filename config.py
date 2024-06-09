import os

# Paths
data_dir       = '/media/storage1/luu/PolyGenSeg/'
real_image_dir = os.path.join(data_dir, 'real', 'images')
real_mask_dir  = os.path.join(data_dir, 'real', 'images-mask')
gen_image_dir  = os.path.join(data_dir, 'generated', 'images')
gen_mask_dir   = os.path.join(data_dir, 'generated', 'images-mask')
train_json     = 'polyp_train.json'
val_json       = 'polyp_valid.json'
test_json      = 'polyp_test.json'

# Data
image_size  = 128
batch_size  = 128
num_workers = 4
pin_memory  = True