describe('Tests of frank-manual config - only IAF_Util', () => {
  it('Test that the only alert in the status page is about config IAF-Util', () => {
    cy.visit('')
	  cy.get('.alert-warning').should('have.length', 1).within(() => {
      cy.contains('Configuration [IAF_Util]').should('have.length', 1)
    })
  })

  it('Test that only alerts are IAF-Util and FrankConfig-compatibility.xsd', () => {
    cy.get('.alert-warning').then((alerts: JQuery<Html>) => {
      const totalNumAlerts = alerts.length
      cy.log(`Total number of Adapter Status alerts is: ${totalNumAlerts}`)
      const alertsNoFrankDoc = alerts.filter((a) => {
        const alertText = a.text()
        const isRelevant = alertText.find('FrankConfig-compatibility') < 0
        cy.log(`Alert with text "${alertText}" relevant: ${isRelevant}`)
        return isRelevant
      })
      cy.wrap(alertsNoFrankDoc).contains('Configuration [IAF_Util]').should('have.length', 1)
    })
  })
})