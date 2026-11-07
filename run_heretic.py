# Wrapper: force trust_remote_code=True for the k2_horizon custom code.
# Heretic 2.0.0 passes trust_remote_code=None on the first load attempt and only
# sets it True for models already in its internal trusted set — for a custom-arch
# model transformers 5 then raises instead of prompting. Heretic loads via
# get_model_class() -> AutoModelForCausalLM, whose from_pretrained is its own
# classmethod (NOT PreTrainedModel.from_pretrained), so patch the Auto classes.
import transformers


def _patch(cls):
    _orig = cls.from_pretrained.__func__

    def from_pretrained(klass, *args, **kwargs):
        if kwargs.get("trust_remote_code", None) is None:
            kwargs["trust_remote_code"] = True
        return _orig(klass, *args, **kwargs)

    cls.from_pretrained = classmethod(from_pretrained)


_patch(transformers.AutoModelForCausalLM)
_patch(transformers.AutoModelForImageTextToText)

from heretic.main import main

main()
