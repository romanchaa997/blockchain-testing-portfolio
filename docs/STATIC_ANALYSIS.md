# Статический анализ смарт-контракта SimpleStorage.sol с использованием Slither
INFO:Detectors:
Version constraint ^0.8.0 contains known severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)
        - FullInlinerNonExpressionSplitArgumentEvaluationOrder
        - MissingSideEffectsOnSelectorAccess
        - AbiReencodingHeadOverflowWithStaticArrayCleanup
        - DirtyBytesArrayToStorage
        - DataLocationChangeInInternalOverride
        - NestedCalldataArrayAbiReencodingSizeValidation
        - SignedImmutables
        - ABIDecodeTwoDimensionalArrayMemory
        - KeccakCaching.
It is used by:
        - ^0.8.0 (contracts/SimpleStorage.sol#2)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity
INFO:Detectors:
Parameter SimpleStorage.set(uint256)._data (contracts/SimpleStorage.sol#7) is not in mixedCase
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#conformance-to-solidity-naming-conventions
INFO:Slither:/home/leksandr/blockchain-testing-portfolio/contracts/SimpleStorage.sol analyzed (1 contracts with 100 detectors), 2 result(s) found

## Инструмент
Для проверки безопасности смарт-контракта использовался [Slither](https://github.com/crytic/slither).

## Команда запуска
Анализ проводился командой:
```sh
slither contracts/SimpleStorage.sol
