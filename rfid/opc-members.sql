CREATE TABLE members (
  "id" INTEGER NOT NULL,
  "firstname" TEXT NOT NULL,
  "lastname" TEXT NOT NULL,
  "tag" TEXT NOT NULL,
  "mobile" INTEGER NOT NULL,
  "email" TEXT NOT NULL,
  "card_id" TEXT NOT NULL
);

.separator ,
.import opc-members.csv members
