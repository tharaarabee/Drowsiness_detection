import os
import numpy as np

# just to unison shuffled copies :)
def USC(a, b):
    p = np.random.permutation(len(a))
    return a[p], b[p]




def Preprocess(path1, WSize, stride, test_fold):
    # المسار 1 هو عنوان المجلد الذي يحوي جميع الموضوعات ، ولكل موضوع ثلاثة ملفات نصية لمستويات التنبيه كشبه النعاس والنعاس
    # WSize decides the length of blink sequence
    # stride is the step by which the moving windo slides over consecutive blinks to generate the sequences
    # test_fold is the number of fold that is picked as test and uses the other folds as training
    # output=[N,T,F]

    path = path1
    folds_list = os.listdir(path1)
    for f, fold in enumerate(folds_list):
        print(fold)
        path1 = path + '/' + fold
        folder_list = os.listdir(path1)
        if fold == test_fold:

            print("Not this fold ;)")
            continue
        for ID, folder in enumerate(folder_list):
            print("#########\n")
            print(str(ID) + '-' + str(folder) + '\n')
            print("#########\n")
            files_per_person = os.listdir(path1 + '/' + folder)
            for txt_file in files_per_person:
                if txt_file == 'alert.txt':
                    alertTXT = path1 + '/' + folder + '/' + txt_file
                    Freq = np.loadtxt(alertTXT, usecols=1)
                    Amp = np.loadtxt(alertTXT, usecols=2)
                    Dur = np.loadtxt(alertTXT, usecols=3)
                    Vel = np.loadtxt(alertTXT, usecols=4)
                    blink_num = len(Freq)
                    bunch_size = blink_num // 3  # one third used for baselining
                    remained_size = blink_num - bunch_size
                    # Using the last bunch_size number of blinks to calculate mean and std
                    u_Freq = np.mean(Freq[-bunch_size:])
                    sigma_Freq = np.std(Freq[-bunch_size:])
                    if sigma_Freq == 0:
                        sigma_Freq = np.std(Freq)
                    u_Amp = np.mean(Amp[-bunch_size:])
                    sigma_Amp = np.std(Amp[-bunch_size:])
                    if sigma_Amp == 0:
                        sigma_Amp = np.std(Amp)
                    u_Dur = np.mean(Dur[-bunch_size:])

                    sigma_Dur = np.std(Dur[-bunch_size:])
                    if sigma_Dur == 0:
                        sigma_Dur = np.std(Dur)
                    u_Vel = np.mean(Vel[-bunch_size:])
                    sigma_Vel = np.std(Vel[-bunch_size:])
                    if sigma_Vel == 0:
                        sigma_Vel = np.std(Vel)
                    print('freq: %f, amp: %f, dur: %f, vel: %f \n' % (u_Freq, u_Amp, u_Dur, u_Vel))



                    # sweep a window over the blinks to chunk


                if txt_file == 'semisleepy.txt':
                    blinksTXT = path1 + '/' + folder + '/' + txt_file
                    Freq = np.loadtxt(blinksTXT, usecols=1)
                    Amp = np.loadtxt(blinksTXT, usecols=2)
                    Dur = np.loadtxt(blinksTXT, usecols=3)
                    Vel = np.loadtxt(blinksTXT, usecols=4)
                    blink_num = len(Freq)



                if txt_file == 'sleepy.txt':
                    blinksTXT = path1 + '/' + folder + '/' + txt_file
                    Freq = np.loadtxt(blinksTXT, usecols=1)
                    Amp = np.loadtxt(blinksTXT, usecols=2)
                    Dur = np.loadtxt(blinksTXT, usecols=3)
                    Vel = np.loadtxt(blinksTXT, usecols=4)
                    blink_num = len(Freq)





            if test_fold != "Fold1":
                start = 0
            else:
                start = 1




    return


# المسار 1 هو عنوان المجلد الذي يحوي جميع الموضوعات ، ولكل موضوع ثلاثة ملفات نصية لمستويات التنبيه كشبه النعاس والنعاس
path1 = 'The Drowsiness Data'
window_size = 30
stride = 2
Training = ""
Testing = ""
