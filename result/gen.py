
import os
import gen_min
import gen_model
import gen_rmse
import gen_rmseg

if __name__ == "__main__":
    probs = [
            "Rastrigin_50"
            ]

    if not os.path.exists("./fig"):
        os.mkdir("./fig")


    for p in probs:
        gen_min.generate(p)
        gen_rmse.generate(p)
        gen_model.generate(p)
        gen_rmseg.generate(p)

