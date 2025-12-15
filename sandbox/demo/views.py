from pathlib import Path

from django.conf import settings
from django.views.generic.edit import FormView
from django.urls import reverse

from .forms import SampleForm


class BasicSampleFormView(FormView):
    template_name = "demo/form.html"
    form_class = SampleForm

    def get_success_url(self):
        return reverse("demo:home")


class ModesSampleFormView(BasicSampleFormView):
    template_name = "demo/modes.html"
    demo_data_dir = settings.PROJECT_PATH / "demo/data"

    def get_context_data(self, **kwargs):
        context = super(ModesSampleFormView, self).get_context_data(**kwargs)
        context.update({
            "codemirror_mode": self.codemirror_mode,
        })
        return context

    def get_initial(self):
        """
        Try to find a demo source for given mode if any, if finded use it to
        fill the demo textarea.
        """
        initial = {}

        if self.kwargs.get("mode", None):
            filepath = self.demo_data_dir / "{}.txt".format(self.kwargs["mode"])
            if filepath.exists():
                initial["foo"] = filepath.read_text()

        return initial

    def get(self, request, *args, **kwargs):
        self.codemirror_mode = kwargs.get("mode", None)
        return super(ModesSampleFormView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.codemirror_mode = kwargs.get("mode", None)
        return super(ModesSampleFormView, self).post(request, *args, **kwargs)
