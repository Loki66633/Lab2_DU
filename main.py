import PIL.Image
import torchvision


transformacije = torchvision.transforms.Compose([
    torchvision.transforms.Resize((480, 640)),
    torchvision.transforms.ColorJitter(hue=.1, saturation=.15, contrast=.15, brightness=.1),
    torchvision.transforms.RandomHorizontalFlip(0.3),
    torchvision.transforms.RandomRotation(5, resample=PIL.Image.BILINEAR),
    torchvision.transforms.RandomGrayscale(0.05),
    torchvision.transforms.RandomAdjustSharpness(0.2),
    torchvision.transforms.RandomEqualize(0.1)
])


dataset = torchvision.datasets.ImageFolder('car_data/train', transform=transformacije)
c = 0


globalCounter = 0
for i in range(3):
    c = 0
    for img, label in dataset:
        location = dataset.imgs[c][0]
        location = location[:len(location) - 4]
        img.save(location+"_expanded"+str(globalCounter)+".jpg", quality=95)
        print("radim")
        c += 1
        globalCounter += 1
