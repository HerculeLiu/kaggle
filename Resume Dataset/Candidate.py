

class Candidate:
    def __init__(self,ID,Resume_str, Resume_html, Category):
        '''
        :param ID: ID of the Candidate
        :param Resume_str: the Resume of the Candidate
        :param Resume_html: the html version of Candidate's Resume
        :param Category: the area that Candidate seeking
        '''
        self.ID = ID
        self.Resume_str = Resume_str
        self.Resume_html = Resume_html
        self.Category = Category
        '''
        applicable: Candidate is applicable or not. [1 = yes, -1 = no, 0 = not decide yet]
        '''
        self.applicable = 0

    ''' get methods '''
    def getID(self):
        return self.ID

    def getResume_str(self):
        return self.Resume_str

    def getResume_html(self):
        return self.Resume_html

    def getCategory(self):
        return self.Category

    def getApplicable(self):
        return self.applicable

    ''' set methods '''
    def Applicable(self):
        self.applicable = 1

    def NotApplicable(self):
        self.applicable = -1

    ''' action methods '''
    # def