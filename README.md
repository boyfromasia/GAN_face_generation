# Generating Anime Faces using StyleGAN

![alt text](screenshots\fakes.png)

## Getting start

Firstly you need to clone NVIDIA StyleGAN repository:

```
git clone https://github.com/NVlabs/stylegan3.git
```

Then just run `streamlit` script:

```
streamlit run streamlit_face_generation.py
```

To get result go to `http://localhost:8501/` and you will see:
![alt text](screenshots\start.png)

To generate Faces just choose Truncation PSI threshold and click
`Generate Face` button. So you will see the results:
![alt text](screenshots\res.png)

All generated faces will be saved in `\out` folder.

## Information about training

Trained model: [Link to download](https://drive.google.com/file/d/1Mi10Li_mpam-2el8GAYwcmZ4nFjKmZLg/view?usp=sharing)

Dataset: [Anime Faces Dataset](https://www.kaggle.com/datasets/splcher/animefacedataset)

Training process:  Takes `4h 13m 02s` and check ~240k images.


