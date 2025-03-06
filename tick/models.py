from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Ticker(Base):
    __tablename__ = "ticker"

    ticker: Mapped[str] = mapped_column(unique=True)
    cik_str: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()


class Token(Base):
    __tablename__ = "token"

    id_token: Mapped[str] = mapped_column()
    access_token: Mapped[str] = mapped_column()
    refresh_token: Mapped[str] = mapped_column()
    token_type: Mapped[str] = mapped_column()
    scope: Mapped[str] = mapped_column()
    expires_in: Mapped[int] = mapped_column()
    access_token_expires: Mapped[float] = mapped_column()
    refresh_token_expires: Mapped[float] = mapped_column()
