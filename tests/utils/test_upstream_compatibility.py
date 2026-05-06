"""
Tests checking for vLLM upstream compatibility requirements.

As we remove support for old vLLM versions, we want to keep track of the
compatibility code that can be cleaned up.
"""

import os

import pytest

pytestmark = pytest.mark.compat

VLLM_VERSION = os.getenv("TEST_VLLM_VERSION", "default")


<<<<<<< HEAD
<<<<<<< HEAD
def test_compilation_times_compat():
    """
    When this test starts failing because CompilationTimes exists in the lowest supported vllm
    version, the try/except import and conditional usage of CompilationTimes in
    spyre_worker.py can be simplified to an unconditional import.
    """
    import vllm.v1.worker.worker_base as worker_base

    if VLLM_VERSION == "vLLM:lowest":
        assert not hasattr(worker_base, "CompilationTimes"), (
            "Backwards compatibility shim for CompilationTimes in spyre_worker.py can be removed"
=======
def test_tokenizer_registry_get_config_patch():
=======
def test_compilation_times_compat():
>>>>>>> chore: add vllm v0.20.0 support and model smoke tests (#952)
    """
    When this test starts failing because CompilationTimes exists in the lowest supported vllm
    version, the try/except import and conditional usage of CompilationTimes in
    spyre_worker.py can be simplified to an unconditional import.
    """
    import vllm.v1.worker.worker_base as worker_base

    if VLLM_VERSION == "vLLM:lowest":
<<<<<<< HEAD
        assert not hasattr(tokenizer_registry, "get_config"), (
            "Backwards compatibility code in _patch_tokenizer_registry_get_config can be removed"
>>>>>>> :bug: Fix mistral tokenizer loads (#951)
=======
        assert not hasattr(worker_base, "CompilationTimes"), (
            "Backwards compatibility shim for CompilationTimes in spyre_worker.py can be removed"
>>>>>>> chore: add vllm v0.20.0 support and model smoke tests (#952)
        )
