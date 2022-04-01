def create_db(base, engine):
    # Create all tables in the engine. This is equivalent to "Create Table"
    base.metadata.create_all(engine)