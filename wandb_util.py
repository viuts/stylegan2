import wandb

def locate_latest_pkl(path):
    api = wandb.Api()
    runs = api.runs(path, order='created_at')
    file_name = None

    # loop for each run to find the lastest model
    for run in runs:
        files = run.files()
        count = 0
        for file in files:
            if '.pkl' in file.name:
                ckpt_count, _ = file.name.split('.')
                if int(ckpt_count) > count:
                    count = int(ckpt_count)
                    file_name = file.name

        if count > 0:
            return '/'.join(run.path), file_name
    return None, None