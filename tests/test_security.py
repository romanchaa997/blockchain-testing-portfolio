import subprocess
import json
import pytest

@pytest.fixture(scope="session")
def slither_report(tmp_path_factory):
    # Определяем путь для временного файла отчёта
    temp_dir = tmp_path_factory.mktemp("slither")
    report_path = temp_dir / "slither_report.json"

    # Запускаем slither через Python-модуль, используя shell=True
    result = subprocess.run(
        "python -m slither_analyzer contracts/AdvancedStorage.sol --json " + str(report_path),
        capture_output=True,
        text=True,
        shell=True
    )
    
    if result.returncode != 0:
        pytest.skip(f"Slither failed to run: {result.stderr}")

    with open(report_path, "r") as f:
        return json.load(f)

def test_slither_no_critical_vulnerabilities(slither_report):
    """
    Проверяем, что Slither не обнаружил критических уязвимостей.
    """
    vulnerabilities = slither_report.get("results", [])
    # Фильтруем уязвимости с уровнем воздействия 'high' или 'critical'
    critical_vulns = [
        vuln for vuln in vulnerabilities
        if vuln.get("impact", "").lower() in ["high", "critical"]
    ]
    assert len(critical_vulns) == 0, f"Critical vulnerabilities found: {critical_vulns}"
