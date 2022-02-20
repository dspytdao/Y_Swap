from pyteal import *


def approval_program():
    on_creation = Seq(
        [
            Assert(Txn.application_args.length() == Int(1)),
            App.globalPut(Bytes("total supply"), Btoi(Txn.application_args[0])),
            App.globalPut(Bytes("reserve"), Btoi(Txn.application_args[0])),
            App.globalPut(Bytes("Creator"), Txn.sender()),
            Return(Int(1)),
        ]
    )

    is_creator = Txn.sender() == App.globalGet(Bytes("Creator"))
    
    on_closeout = Seq(
        [
            App.globalPut(
                Bytes("reserve"),
                App.globalGet(Bytes("reserve"))
                + App.localGet(Int(0), Bytes("balance")),
            ),
            Return(Int(1)),
        ]
    )

    register = Seq([
        App.localPut(Int(0), Bytes("balance"), Int(0)),
        Return(Int(1))
    ])

    get_mint = Btoi(Txn.application_args[1])
    mint = Seq(
        [
            If(
                And(
                    Txn.application_args.length() == Int(2),
                    get_mint > Int(0)
                ),
                App.globalPut(
                    Bytes("reserve"), App.globalGet(Bytes("reserve")) - get_mint,
                ),
            ),
            App.localPut(
                Int(0),
                Bytes("balance"),
                get_mint,
            ),
            Return(is_creator),
        ]
    )

    # transfer assets from the sender to Txn.accounts[1]
    transfer_amount = Btoi(Txn.application_args[1])
    transfer = Seq(
        [
            If(
                And(
                    Txn.application_args.length() == Int(2),
                    transfer_amount > Int(0),
                    transfer_amount <= App.localGet(Int(0), Bytes("balance"))
                ),
                App.globalPut(
                    Bytes("reserve"), App.globalGet(Bytes("reserve")) + get_mint,
                ),
            ),      
            App.localPut(
                Int(0),
                Bytes("balance"),
                App.localGet(Int(0), Bytes("balance")) - transfer_amount,
            ),
            Return(Int(1)),
        ]
    )

    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication, Return(is_creator)],
        [Txn.on_completion() == OnComplete.UpdateApplication, Return(is_creator)],
        [Txn.on_completion() == OnComplete.CloseOut, on_closeout],
        [Txn.on_completion() == OnComplete.OptIn, register],
        [Txn.application_args[0] == Bytes("mint"), mint],
        [Txn.application_args[0] == Bytes("transfer"), transfer],
    )

    return program


def clear_state_program():
    program = Seq(
        [
            App.globalPut(
                Bytes("reserve"),
                App.globalGet(Bytes("reserve"))
                + App.localGet(Int(0), Bytes("balance")),
            ),
            Return(Int(1)),
        ]
    )

    return program


if __name__ == "__main__":
    with open("asset_approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    with open("asset_clear_state.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)