import db
import re

async def add_request(ctx, name: str, questions: str):

    """
        command to add regrade request
        Parameters:
            ctx : context of function activation
            name: name of the student
            questions: question numbers to be regraded
            output: adds the regrade request to the database
    """
    name = name.upper()

    for name, questions in db.select_query(
            '''SELECT name,questions FROM regrade WHERE name=? ''',
            (name,)

    ):
        if name:
            await ctx.send("Duplicate regrade request. Use !regrade-update command to make updates to request")
            return


    if not re.match(r"[Qq][0-9]+,[Qq][0-9]+", questions):
        await ctx.send("Invalid Input. Enter valid question numbers")
    else:
        db.mutation_query(
            'INSERT INTO regrade VALUES (?, ?, ?)',
            [ctx.guild.id, name, questions]
        )
        await ctx.send(name + "'s regrade request successfully submitted")
