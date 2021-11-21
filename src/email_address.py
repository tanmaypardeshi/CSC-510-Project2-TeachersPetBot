import db


async def create_email(ctx, email_address):
    author_id = ctx.message.author.id
    fetch_query = 'SELECT author_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    data = cur.fetchone()
    if data:
        await ctx.send('There is already an email address configured for this user. '
                       'Please update it using update_email command')
        return
    insert_query = 'INSERT INTO email_address VALUES (?, ?, ?)'
    db.mutation_query(insert_query, [author_id, email_address, 1])
    await ctx.send('Email has been configured successfully!')


async def update_email(ctx, email_address):
    author_id = ctx.message.author.id
    fetch_query = 'SELECT author_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    data = cur.fetchone()
    if data:
        update_query = 'UPDATE email_address SET email_id=? WHERE author_id=? and is_active=?'
        db.mutation_query(update_query, (email_address, author_id, 1,))
        await ctx.send('Email address has been updated successfully')
        return
    await ctx.send('There is no configured email address')


async def view_email(ctx):
    author_id = ctx.message.author.id
    fetch_query = 'SELECT email_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    email_address = cur.fetchone()
    if email_address:
        await ctx.send('Configured email address : {0}'.format(email_address[0]))
        return
    await ctx.send('There is no configured email address')

