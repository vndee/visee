import re
import base64
from PIL import Image
from io import BytesIO
from torchvision import transforms

from common.logger import get_logger
from indexer.feature_extractor.efficientnet import EfficientNet

logger = get_logger(logger_name=__name__)


class FeatureExtractor:
    def __init__(self, arch='efficientnet-b7'):
        '''
        Load pretrained model for EfficientNet features extractor.
        '''

        logger.info('Load %s' % arch)
        try:
            self.model = EfficientNet.from_pretrained(arch)
        except Exception as ex:
            self.model = None
            logger.error('Failed to load %s' % arch)
            logger.exception(ex)

        self.image_size = EfficientNet.get_image_size(arch)

    def extract(self, img):
        '''
        Extract features in image, input must be a base64 encoded object.
        '''
        
        logger.info('Start features extraction')
        try:
            img = FeatureExtractor.base64toPIL(img)
            logger.info(f'Decode {img.mode} successfully')
        except Exception as ex:
            logger.error('Input must be a base64 encoded object')
            logger.exception(ex)
            return None

        # preprocess image
        tfms = transforms.Compose([transforms.Resize(self.image_size), transforms.CenterCrop(self.image_size),
                                    transforms.ToTensor(), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]), ])
        img = tfms(img).unsqueeze(0)

        feat = self.model.extract_features(img).squeeze(0)
        return feat.mean(dim=1).mean(dim=1).detach().numpy()

    @staticmethod
    def base64toPIL(b64):
        return Image.open(BytesIO(base64.b64decode(b64)))

    @staticmethod
    def base64_verify(b64):
        return re.match(r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$', b64)


if __name__ == '__main__':
    path = '/media/vndee/DATA/workspace/vndee/product-seeker/data/https_3A_2F_2Fgearlaunch-product-images.imgix.net_2Fimg_2Fproduct_2FUnisexCrew_FRONT_46be88da32_c5e5c699-c087-4cf9-8bcc-e4a9c0aea221_550x825.webp'
    with open(path, 'rb') as img_file:
        encoded_string = base64.b64encode(img_file.read())
    
    fte = FeatureExtractor()
    # ans = torch.flatten(fte.extract(encoded_string)).detach().numpy()
    ans = fte.extract(encoded_string)
    print(ans.shape)
