#!/usr/bin/env python3
# Copyright 2022 Canonical
# See LICENSE file for licensing details.
import logging

import pytest

log = logging.getLogger(__name__)


@pytest.mark.abort_on_fail
@pytest.mark.skip_if_deployed
async def test_build_and_deploy(ops_test, series):
    """Build prometheus-apt-exporter charm and deploy it in bundle."""
    prometheus_apt_exporter_charm = await ops_test.build_charm(".")

    await ops_test.model.deploy(
        ops_test.render_bundle(
            "tests/integration/bundle.yaml.j2",
            prometheus_apt_exporter_charm=prometheus_apt_exporter_charm,
            series=series,
        )
    )
    await ops_test.model.wait_for_idle()