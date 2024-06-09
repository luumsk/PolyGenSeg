from torch.utils.data import Dataset
from torchvision.io import read_image
from torchvision.transforms import functional as F

import config as cfg
import utils as ut

class GeneratedPoLypDataset(Dataset):
    def __init__(self, image_paths):
        self.image_paths = sorted(image_paths)
        self.len = len(self.image_paths)

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        # Load image
        image_path = self.image_paths[idx]
        image = read_image(image_path)

        # Load mask
        mask_path = ut.convert_to_mask_path(image_path)
        mask = read_image(mask_path)

        # Resize image and mask
        image = F.resize(image, (cfg.image_size, cfg.image_size))
        mask  = F.resize(mask, (cfg.image_size, cfg.image_size))

        # The generated image has 4 channels
        # 3 first channels are RGB, the last is a black background
        # Return only 1 channel of image
        if image.shape[0] > 3:
            image = image[:3,...]

        # The generated mask has 4 channels
        # The first 3 channels are binary mask, the last is a black background
        # Return only 1 channel of mask
        if mask.shape[0] > 1:
            mask = mask[0,...]

        # Normalize image and mask
        #image = self.normalize(image)
        mask  = mask / 255.0

        return image.float(), mask.int()