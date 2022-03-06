from dao.sqlBase import sqlbase


class studentActions():
    @staticmethod
    def insertStudent(FirstName, LastName, BirthdayDate, Gender, NationalCode, BirthdayPlace, Weight, Height, PreEducation, DominantHand, Insurance, FamilyMembers, MemberNum, Supervisor, SpecialDisease, Medicine, HomeAddress, Country, City):
        # connect to database
        sqlBase = sqlbase()
        connection, cursor = sqlBase.getConnection()

        # Run command
        cursor.execute(f"set nocount on; INSERT INTO Students(FirstName, LastName, BirthdayDate, Gender, NationalCode, BirthdayPlace, Weight, Height, PreEducation, DominantHand, Insurance, FamilyMembers, MemberNum, Supervisor, SpecialDisease, Medicine, HomeAddress, Country, City) VALUES('{FirstName}', '{LastName}', '{BirthdayDate}', '{Gender}', '{NationalCode}', '{BirthdayPlace}', '{Weight}', '{Height}', '{PreEducation}', '{DominantHand}', '{Insurance}', '{FamilyMembers}', '{MemberNum}', '{Supervisor}', '{SpecialDisease}', '{Medicine}', '{HomeAddress}', '{Country}', '{City}')")

        connection.commit()

        cursor.close()
        connection.close()
        return True


