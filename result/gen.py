
import os
import gen_min
import gen_model
import gen_rmse

if __name__ == "__main__":
    probs = [
            "Schwefel_100"
            ]

    if not os.path.exists("./fig"):
        os.mkdir("./fig")


    for p in probs:
        gen_min.generate(p)
        gen_rmse.generate(p)
        gen_model.generate(p)

