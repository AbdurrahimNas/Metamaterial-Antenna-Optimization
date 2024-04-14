from django.shortcuts import render
from optimizationapp.models import Metamaterial
from optimizationapp.forms import MetamaterialForm
import joblib

# Create your views here.


def optimize(request):
    if request.method=="POST":
        form = MetamaterialForm(request.POST)
        if form.is_valid():
            form.save()
            model = joblib.load("./metametarial_antennas.pkl")
            form_fields = list(form.cleaned_data.values())
            prediction = model.predict([form_fields])
            return render(request, "optimizationapp/optimize.html", {"form": form, "s":prediction[0][0], "pr": prediction[0][1], "p0":prediction[0][2]})
    form = MetamaterialForm()

    return render(request, "optimizationapp/optimize.html", {"form": form})

