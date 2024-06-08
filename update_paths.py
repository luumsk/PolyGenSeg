import json, os
from pathlib import Path

def convert_path(path_str, new_root_dir):
    path = Path(path_str)
    new_root_dir = Path(new_root_dir)

    absolute_original_path = path.resolve()
    relative_path = absolute_original_path.relative_to(Path('.').resolve())
    new_absolute_path = new_root_dir / relative_path

    return str(new_absolute_path)

def load_json(path):
    data = None
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def check_path(path):
    if not os.path.isfile(path):
        raise ValueError(f'File does not exist: {path}')

def main(json_paths, new_root_dir, disable_checkpath=False):
    for json_path in json_paths:
        # Load json
        images = load_json(json_path).get('images')

        # Save original images as backups
        save_json(
            path=json_path.replace('.json', '_old.json'),
            data={'images': images}
        )

        # Copy images
        new_images = images[:]

        for new_image in new_images:
            # Convert image path
            new_image_path = convert_path(
                new_image.get('image_path'),
                new_root_dir
            )
            if not disable_checkpath: check_path(new_image_path)
            new_image['image_path'] = new_image_path

            # Convert mask path
            new_mask_path = convert_path(
                new_image.get('mask_path'),
                new_root_dir
            )
            if not disable_checkpath: check_path(new_mask_path)
            new_image['mask_path'] = new_mask_path

        # Save new images with converted paths
        save_json(
            path=json_path,
            data={'images': new_images}
        )
        

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Replace the root directory of given JSON files.'
    )
    parser.add_argument('--json', metavar='-j', type=str, nargs='+',
                        dest='json_files',
                        help='Input polyp JSON files (can be multiple)')
    parser.add_argument('--newDir', metavar='-n', type=str,
                        dest='new_root_dir',
                        help='New root directory to replace with')
    parser.add_argument('--disable_checkpath', action='store_true',
                        dest='disable_checkpath', default=False,
                        help='Disable checking if the output paths exist')
    
    args = parser.parse_args()
    
    main(args.json_files, args.new_root_dir, args.disable_checkpath)
