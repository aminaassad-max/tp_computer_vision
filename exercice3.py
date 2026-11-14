from google.colab import files
from google.colab.patches import cv2_imshow  
uploaded = files.upload()
import cv2 
import torch 
from detectron2.engine import DefaultPredictor 
from detectron2.config import get_cfg 
from detectron2 import model_zoo 
from detectron2.utils.visualizer import Visualizer 
from detectron2.data import MetadataCatalog 
from google.colab.patches import cv2_imshow 
 
# Configuration du modèle pré-entraîné 
CONFIG = "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml" 
 
cfg = get_cfg() 
cfg.merge_from_file(model_zoo.get_config_file(CONFIG)) 
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5 
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(CONFIG) 
# cfg.MODEL.DEVICE = "cpu"   # si pas de GPU 
 
predictor = DefaultPredictor(cfg) 
 
# Charger une image 
img = cv2.imread("Animaux-sauvages.jpg") 
 
# Prédiction 
outputs = predictor(img) 
 
# Visualisation 
v = Visualizer(img[:, :, ::-1], 
MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2) # BGR -> RGB 
out = v.draw_instance_predictions(outputs["instances"].to("cpu")) 
# cv2.imshow("Détection d'objets", out.get_image()[:, :, ::-1]) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 
cv2_imshow(out.get_image()[:, :, ::-1]) 