from selene import browser, have
import os.path


def test_form():
    browser.element('[id="firstName"]').type('Anna')
    browser.element('[id="lastName"]').type('Chayko')

    browser.element('[id="userEmail"]').type('al.nchko@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').type('9102906632').press_tab()

    browser.element('[class="react-datepicker__month-select"]').element('[value="0"]').click()
    browser.element('[class="react-datepicker__year-select"]').element('[value="2000"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--013"]').click()

  #  browser.element('[class=" mr-sm-2 form-control"]').type('89102906632')

    browser.element('[id="subjectsInput"]').type('A')
    browser.all('.subjects-auto-complete__menu').element_by(have.text('Arts')).click()
    browser.element('[id="subjectsInput"]').type('S')
    browser.all('.subjects-auto-complete__menu').element_by(have.text('Computer Science')).click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('[id="uploadPicture"]').set_value(os.path.abspath("../tests/shutterstock_2331893385.jpg"))

    browser.element('[id="currentAddress"]').type('Улица Пушкина, дом Колотушкина')
    browser.element('[id="state"]').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('[id="city"]').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('[id="submit"]').click()

    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

    browser.element('[class="table-responsive"]').should(have.text('Anna Chayko'))
    browser.element('[class="table-responsive"]').should(have.text('al.nchko@gmail.com'))
    browser.element('[class="table-responsive"]').should(have.text('9102906632'))
    browser.element('[class="table-responsive"]').should(have.text('13 January,2000'))

    browser.element('[class="table-responsive"]').should(have.text('Arts'))
    browser.element('[class="table-responsive"]').should(have.text('Computer Science'))
    browser.element('[class="table-responsive"]').should(have.text('Sports'))
    browser.element('[class="table-responsive"]').should(have.text('Reading'))

    browser.element('[class="table-responsive"]').should(have.text('shutterstock_2331893385.jpg'))

    browser.element('[class="table-responsive"]').should(have.text('Улица Пушкина, дом Колотушкина'))
    browser.element('[class="table-responsive"]').should(have.text('NCR Gurgaon'))
