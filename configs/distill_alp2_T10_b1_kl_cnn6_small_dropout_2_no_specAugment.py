config = {
    'batchsize': 32,
    'num_workers': 4,
    'reload': False,
    'net': 'Cnn6_Ours_60k',
    'teacher_net': 'Cnn6_Orig',
    'teacher_path': '/root/no_backup/dcase_challenge/configs.cnn6_orig_dropout_2_specAugment_128_2_16_2/ckpt.pth',
    'kd_loss_type': 'at',
    'kd_alpha': 0.2,
    'temperature': 10.0,
    'kd_beta': 1.0,
    'dropout': 0.2,
    'specAugment': None,
    'lr': 1e-3,
    'eta_min': 1e-5,
    'max_epoch': 200,
    'weight_decay': 1e-5,
}
