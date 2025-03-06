# Static analysis of the SimpleStorage.sol smart contract using Slither
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

## Tool
To check the security of the smart contract, we used [Slither](https://github.com/crytic/slither).

## Launch command
Analysis was carried out by a command:
```sh
slither contracts/SimpleStorage.sol
