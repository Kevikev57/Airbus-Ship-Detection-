In [1]: BATCH_SIZE = 4
        EDGE_CROP = 16
        NB_EPOCHS = 5
        GAUSSIAN_NOISE = 0.1
        UPSAMPLE_MODE = 'SIMPLE'
        # downsampling inside the network
        NET_SCALING = None
        # downsampling in preprocessing
        IMG_SCALING = (1, 1)
        # number of validation images to use
        VALID_IMG_COUNT = 400
        # maximum number of steps_per_epoch in training
        MAX_TRAIN_STEPS = 200
        AUGMENT_BRIGHTNESS = False
