import re
import db


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

    for temp_name in db.select_query(
            '''SELECT name,questions FROM regrade WHERE name=? ''',
            (name,)

    ):
        if temp_name:
            await ctx.send("Duplicate regrade request."\
                    "Use !regrade-update command to make updates to request")
            return

    if not re.match(r"[Qq][0-9]+,[Qq][0-9]+", questions):
        await ctx.send("Invalid Input. Enter valid question numbers")
    else:
        db.mutation_query(
            'INSERT INTO regrade VALUES (?, ?, ?)',
            [ctx.guild.id, name, questions]
        )
        await ctx.send(name + "'s regrade request successfully submitted")


async def display_requests(ctx):
    """
        command to display all the  regrade requests
        Parameters:
            ctx : context of function activation
            output: displays the student name and the question numbers to be regraded
    """
    for name, questions in db.select_query(
            'SELECT name,questions FROM regrade'
    ):
        if name:
            await ctx.send(name + " " + questions)
        else:
            await ctx.send('There are no regrade requests at the moment')
            break
